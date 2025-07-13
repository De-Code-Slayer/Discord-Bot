import unittest
from unittest.mock import AsyncMock, patch

class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_on_member_join(self):
        mock_member = AsyncMock(name="TestUser", id=12345)
        mock_bot = AsyncMock()
        
        # Call the event handler manually
        from bot import on_member_join
        await on_member_join(mock_member)
        
        # Verify the admin DM was attempted
        mock_bot.fetch_user.assert_called_once()