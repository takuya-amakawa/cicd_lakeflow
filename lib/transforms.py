"""ビジネスロジック。Spark に依存しないピュア関数として切り出し、CI で高速にテストする。"""


def categorize_amount(amount: int) -> str:
    """取引金額を4区分に分類する（境界は未満で判定）。

    - 1,000 未満: small
    - 1,000 以上 10,000 未満: medium
    - 10,000 以上 100,000 未満: large
    - 100,000 以上: xlarge
    """
    if amount < 0:
        raise ValueError(f"amount must be non-negative, got {amount}")
    if amount < 1_000:
        return "small"
    if amount < 10_000:
        return "medium"
    if amount < 100_000:
        return "large"
    return "xlarge"
