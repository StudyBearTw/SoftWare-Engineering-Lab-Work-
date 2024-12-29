class Book:
    def __init__(self, bname : str, isbn : str, price : int):
        self._bname = bname
        self._isbn = isbn
        self._price = price

    def get_bname(self) ->str:
        return self._bname
    
    def get_isbn(self) -> str:
        return self._isbn
    
    def get_price(self) -> int:
        return self._price
    
    def get_shipping(self) -> int:
        return 50 if self._price > 100 else 20
    
if __name__ == "__main__":
    # 創建兩本書的實例
    w1 = Book("BOOK1", "ISBN1", 85)
    w2 = Book("BOOK2", "ISBN2", 135)
    
    # 格式化並輸出第一本書的資訊 (書名, ISBN, 價格+運費)
    str1 = f"{w1.get_bname()},{w1.get_isbn()},{w1.get_price() + w1.get_shipping()}"
    # 格式化並輸出第二本書的資訊
    str2 = f"{w2.get_bname()},{w2.get_isbn()},{w2.get_price() + w2.get_shipping()}"
    
    # 打印結果
    print(f"{str1},{str2}")
    