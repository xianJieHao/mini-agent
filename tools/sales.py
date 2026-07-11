# tools/sales.py

from tools.tool import Tool


class SalesTool(Tool):

    @property
    def name(self):
        return "SalesTool"

    @property
    def description(self):
        return "统计销售数据"

    def execute(self, month):
        return f"{month}月销售冠军:A公司" 