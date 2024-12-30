import redis
from typing import Any, Optional
# from redis_user import RedisUser  # RedisUserを別ファイルからインポート
from config import REDIS_URL

class RedisClient:
    def __init__(self, host: Optional[str] = None, port: Optional[int] = None, db: int = 0):
        """
        Redisクライアントの初期化。
        環境変数 `REDIS_URL` が設定されている場合は優先的に使用。
        """
        # Render環境では REDIS_URL が設定されていることが多い
        redis_url = REDIS_URL
        if redis_url:
            self.client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
        else:
            # 環境変数がない場合は引数から接続設定を取得
            self.client = redis.StrictRedis(
                host=host or "localhost",
                port=port or 6379,
                db=db,
                decode_responses=True
            )