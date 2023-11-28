from backend.domain.entitys.budget import Budget

async def test_should_create_a_budget():
    budget = Budget.create(
        titile="teste de budget",
        description="Descrição do orçamento",
        client="1"
    )
    
    assert budget