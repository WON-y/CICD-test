import pytest
from src.cart import Cart, EmptyCartError

def test_empty_cart_raises():
    with pytest.raises(EmptyCartError):
        Cart().total()  # 빈 카트에서 total() 호출 시 EmptyCartError가 발생하는지 검증

def test_total_sums_items(cart):  # 함수의 매개변수 이름과 fixture 이름(cart)을 일치시킴
    cart.add("book", 12000, 2)
    assert cart.total() == 24000

def test_negative_price_rejected():
    cart = Cart()
    with pytest.raises(ValueError, match="price must be"):
        cart.add("book", -100)
        
# import logging


# def test_error_is_logged(cart, caplog):
#     # caplog: logging 모듈의 로그 출력을 가로채는 내장 픽스처
#     with caplog.at_level(logging.ERROR):  # ERROR 레벨 이상의 로그만 캡처
#         try:
#             cart.total()
#         except Exception:
#             logging.getLogger("app").exception("빈 장바구니 결제 시도")

#     assert "빈 장바구니" in caplog.text  # 로그 메시지 텍스트 검증
#     assert caplog.records[0].levelname == "ERROR"  # 로그 레벨 검증







# def test_env(monkeypatch):
#     # monkeypatch: 환경 변수, 모듈 속성 등을 안전하게 임시 변경
#     monkeypatch.setenv("ENV", "test")
#     import os

#     assert os.getenv("ENV") == "test"






# def test_save_report(tmp_path):
#     # tmp_path: pathlib.Path 객체로 제공되는 pytest 내장 임시 디렉터리
#     f = tmp_path / "report.txt"
#     f.write_text("매출 1000", encoding="utf-8")
#     assert f.read_text(encoding="utf-8").startswith("매출")






# @pytest.mark.parametrize(
#     "price, qty, expected",
#     [
#         (12000, 2, 24000), # 1번 케이스
#         (0, 5, 0), # 2번 케이스
#         (1000, 1, 1000), # 3번 케이스
#     ],
# )
# def test_total(cart, price, qty, expected):
#     cart.add("item", price, qty)
#     assert cart.total() == expected






# def test_first(cart):
#     cart.add("book", 1000)
#     assert len(cart.items) == 1 # 통과 (아이템 1개 들어감)
# def test_second(cart):
#     assert len(cart.items) == 0 # 실패! (앞 테스트가 넣은 'book'이 그대로 남아 있음) -> pytest fixture의 scope="function"이 기본값이므로, 각 테스트 함수마다 새로운 Cart 인스턴스를 생성해야 함






# @pytest.mark.xfail(reason="알려진 버그")
# def test_total_sums_items():
#     cart = Cart()
#     cart.add("book", 12000, 2)
#     assert cart.total() == 24000

# def test_total_sums_items(cart): # 함수의 매개변수 이름과 fixture 이름(cart)을 일치시킴
#     cart.add("book", 12000, 2)
#     assert cart.total() == 24000

# #@pytest.mark.skipif(sys.platform == "win32", reason="윈도우에서는 테스트하지 않음")
# def test_empty_cart_raises():
#     with pytest.raises(EmptyCartError):
#         Cart().total()

# #@pytest.mark.skip(reason="개발 중")
# def test_negative_price_rejected():
#     cart = Cart()
#     with pytest.raises(ValueError, match="price must be"):
#         cart.add("book", -100)