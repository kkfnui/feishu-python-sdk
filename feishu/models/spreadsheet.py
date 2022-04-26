#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""spreadsheet 类型"""

from typing import List, Optional, Any

from pydantic import BaseModel


class SpreadSheetValueRange(BaseModel):
    """
     {
        "majorDimension":"ROWS",
        "range":"208db0!A1:D4",
        "revision":17,
        "values":[
            [
                "id",
                "country",
                "product",
                null
            ]
        ]
    }
    """
    majorDimension: str
    range: str
    revision: int
    values: List[Any]


class SpreadSheetOneRangeResponse(BaseModel):
    """
    {
        "revision":17,
        "spreadsheetToken":"shtcnRuDIpgw9VvLxNBoxLSWwfb",
        "valueRange": SpreadSheetValueRange
    }
    """
    revision: int
    spreadsheetToken: str
    valueRange: SpreadSheetValueRange