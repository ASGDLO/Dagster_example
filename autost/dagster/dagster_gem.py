import json
import os
from typing import List

from autost.data.rebalancedate import RebalanceChecker
from autost.configuration.strategies_list import RATBScriptExecutor
from autost.trigger.stg_codetrigger import RunTriggerChecker
from dagster import op, job, schedule, repository, DefaultScheduleStatus


def load_strategies_from_config(config_path: str) -> List[dict]:
    with open(config_path, 'r') as file:
        all_strategies = json.load(file)

    selected_docker_id = os.getenv('DOCKER_ID')
    if selected_docker_id:
        strategies = [
            s for s in all_strategies if s.get('docker_id') == selected_docker_id
        ]
    else:
        strategies = all_strategies

    return strategies


def create_op_for_strategy(strategy_name: str) -> callable:
    @op(name=f"{strategy_name}_run")
    async def strategy_op(context):
        checker = RATBScriptExecutor()
        await checker.execute(strategy_name)

    return strategy_op


def create_job_for_strategy(strategy: dict) -> callable:
    strategy_op = create_op_for_strategy(strategy['strategy_name'])

    @job(name=f"{strategy['strategy_name']}_job")
    def strategy_job():
        strategy_op()

    return strategy_job


def create_scheduler_for_strategy(strategy: dict, dynamic_job: callable) -> callable:
    @schedule(
        cron_schedule=strategy['cron_schedule'],
        job=dynamic_job,
        default_status=DefaultScheduleStatus.RUNNING,
        execution_timezone=strategy['execution_timezone'],
        name=f"{strategy['strategy_name']}_schedule"
    )
    def strategy_scheduler(context):
        checker = RebalanceChecker()
        trigger = RunTriggerChecker(checker, strategy['map'], context)
        return trigger.trigger_if_condition_met()

    return strategy_scheduler


@repository
def my_repository():
    config_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'config.json'
    )
    strategies = load_strategies_from_config(config_path)

    dynamic_entities = []
    for strategy in strategies:
        job = create_job_for_strategy(strategy)
        scheduler = create_scheduler_for_strategy(strategy, job)
        dynamic_entities.extend([job, scheduler])

    return dynamic_entities
