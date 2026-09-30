import unittest

from retrybox import retry, try_retry


class RetryboxTest(unittest.TestCase):
    def test_succeeds_on_second(self) -> None:
        state = {"n": 0}

        def flaky() -> str:
            state["n"] += 1
            if state["n"] < 2:
                raise RuntimeError("nope")
            return "ok"

        self.assertEqual(retry(flaky, 3), "ok")

    def test_try_retry(self) -> None:
        ok, value = try_retry(lambda: "ok", 1)
        self.assertEqual((ok, value), (True, "ok"))
        def boom() -> str:
            raise ValueError("x")

        failed, err = try_retry(boom, 1)
        self.assertFalse(failed)
        self.assertIsInstance(err, ValueError)

    def test_gives_up(self) -> None:
        def always() -> None:
            raise ValueError("x")

        with self.assertRaises(ValueError):
            retry(always, 2)


if __name__ == "__main__":
    unittest.main()
