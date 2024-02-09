import asyncio

async def calcula_imposto(faturamento):
    print(faturamento * 0.1)


async def calcula_bonus_funcionario(vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "Bonus:", venda * 0.05)
        await asyncio.sleep(1)


async def fechamento():
    vendas = {
        'João': 100,
        'Maria': 200,
        'Pedro': 300
    }
    faturamento = 1000

    task1 = asyncio.create_task(calcula_bonus_funcionario(vendas))
    task2 = asyncio.create_task(calcula_imposto(faturamento))
    print('Fechamento finalizado!')
    await task1
    await task2


asyncio.run(fechamento())
