import asyncio


class RATBScriptExecutor:
    def __init__(self):
        # Configuration mapping method names to script paths and countdown seconds
        self.scripts = {
            'script_1': ('algo/script_1.py', 5),
            'script_2': ('algo/script_2.py', 6),
            'script_3': ('quant/script_3.py', 6),
            'script_4': ('algo/script_4.py', 6),
            'script_5': ('quant/script_5.py', 6),
            'script_6': ('algo/script_6.py', 6),
            'script_7': ('quant/script_7.py', 6),
            'script_8': ('algo/script_8.py', 6),
            'script_9': ('algo/script_9.py', 6),
            'script_10': ('algo/script_10.py', 6),
            'script_11': ('algo/script_11.py', 6),
            'script_12': ('algo/script_12.py', 6),
            'script_13': ('quant/script_13.py', 6),
            'script_14': ('quant/script_14.py', 6),
            'script_15': ('quant/script_15.py', 6),
            'script_16': ('quant/script_16.py', 6),
            'script_17': ('quant/script_17.py', 6),
            'script_18': ('quant/script_18.py', 6),
            'script_19': ('quant/script_19.py', 6),
            'script_20': ('quant/script_20.py', 6),
            'script_21': ('quant/script_21.py', 6),
            'script_22': ('quant/script_22.py', 6),
            'script_23': ('quant/script_23.py', 6),
            'script_24': ('quant/script_24.py', 6),
            'script_25': ('quant/script_25.py', 6),
            'script_26': ('quant/script_26.py', 6),
            'script_27': ('quant/script_27.py', 6),
            'script_28': ('quant/script_28.py', 6),
            'script_29': ('quant/script_29.py', 6),
        }

    async def _execute_script_with_countdown(self, script_name, countdown_seconds):
        print(f"Executing {script_name} now. Running {script_name}...")

        try:
            # Asynchronously execute the script
            process = await asyncio.create_subprocess_exec(
                'python', script_name,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            # Optional: Implement countdown using asyncio.sleep
            await asyncio.sleep(countdown_seconds)

            stdout, stderr = await process.communicate()

            print(f"{script_name} Script Output:")
            print(stdout.decode())

            if stderr:
                print("Script Errors:")
                print(stderr.decode())

        except Exception as e:
            print(f"An error occurred while executing {script_name}: {e}")

    async def execute(self, method_name):
        """Execute a script based on the method name asynchronously."""
        script_info = self.scripts.get(method_name)
        if script_info:
            script_name, countdown = script_info
            await self._execute_script_with_countdown(script_name, countdown)
        else:
            print(f"No script found for method: {method_name}")


