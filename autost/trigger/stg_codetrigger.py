import datetime
from dagster import RunRequest
import pandas as pd


class RunTriggerChecker:
    def __init__(self, checker, stg_code_map, log_context):
        self.checker = checker
        self.stg_code_map = stg_code_map
        self.log_context = log_context

    async def trigger_if_condition_met(self):
        try:
            kr, us = await self.checker.get_rebalance_date()
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            self.log_context.log.info(f"Today's date: {today}")

            combined_df = pd.concat([kr, us])
            matching_rows = combined_df[combined_df['work_days'] == today]

            for stg_code in matching_rows['STG_CODE'].unique():
                if stg_code in self.stg_code_map:
                    self.log_context.log.info("Condition met, triggering RunRequest")
                    return RunRequest(run_key=None, run_config={})
                    
            self.log_context.log.info("No matching condition found, returning None")
        except Exception as e:
            self.log_context.log.error(f"Error occurred: {e}")

        return None
