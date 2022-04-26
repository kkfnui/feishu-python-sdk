#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""电子表格相关API

包括:
- 读取电子表格

"""
from typing import List, Optional

from .base import BaseAPI, allow_async_call
from ..consts import FEISHU_BATCH_SEND_SIZE
from ..models import BotInfo, CreateChatRequest, SpreadSheetOneRangeResponse, ChatPagination, ChatInfo, ChatUpdateRequest, \
    AddChatterResponse, RemoveChatterResponse


class SpreeadSheetAPI(BaseAPI):

    @allow_async_call
    def retrieve_one_range(self, spreadsheetToken: str, range: str) -> SpreadSheetOneRangeResponse:
        """读取单个范围
        https://open.feishu.cn/document/ukTMukTMukTM/ugTMzUjL4EzM14COxMTN
        Args:
            spreadsheetToken: spreadsheet 的 token
            range: 查询范围，包含 sheetId 与单元格范围两部分

        Returns:
            SpreadSheetOneRangeResponse
        失败会raise FeishuError, (code和msg对应飞书平台的code/msg)
        """
        api = "/sheets/v2/spreadsheets/%s/values/%s" %(spreadsheetToken, range)


        result = self.client.request("GET", api=api)


        return SpreadSheetOneRangeResponse(**result.get("data"))

