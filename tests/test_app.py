# 必要なモジュールをインポート
from fastapi.testclient import TestClient  # FastAPIのテストクライアント
from fast_test_2.main import app  # FastAPIアプリケーションのインスタンス

# TestClientを作成してアプリケーションと連携
client = TestClient()

# テストケースを定義
def test_read_root():
    # "/" エンドポイントにGETリクエストを送信してレスポンスを取得
    response = client.get("/")
    
    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200
    
    # レスポンスのJSONが期待通りであることを確認
    assert response.json() == {"message": "Hello, world!"}
