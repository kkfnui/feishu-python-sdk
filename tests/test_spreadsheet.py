import asyncio
import sys
from feishu import FeishuClient

import pandas as pd
import numpy as np

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
cli = FeishuClient(run_async=False)
cli_async = FeishuClient(run_async=True)



def test_retrieve_one_range():
    # bot_info = cli.retrieve_one_range("shtcnRuDIpgw9VvLxNBoxLSWwfb", "208db0")
    # import json
    # print(json.dumps(bot_info.valueRange.values))

    load_dataframe_from_spreadsheet("shtcnRuDIpgw9VvLxNBoxLSWwfb", "208db0")


def load_dataframe_from_spreadsheet(token, range, dftype=0):
    resp = cli.retrieve_one_range("shtcnRuDIpgw9VvLxNBoxLSWwfb", "208db0")
    values = resp.valueRange.values

    for item in values[0]:
        if item is None:
            raise ValueError("Has None value in first row.")

    df2 = pd.DataFrame(np.array(values[2:]), columns=values[0])
    print(df2)
    pass

if __name__ == "__main__":
    test_retrieve_one_range()

