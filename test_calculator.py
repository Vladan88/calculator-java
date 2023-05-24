def test_calculate():
    expression = "4+5*2-3/1"
    expected_result = 10.0

    result = Calculator.Run(expression)

    assert float(result) == expected_result, "Rezultat nije jednak očekivanom rezultatu."

test_calculate()
