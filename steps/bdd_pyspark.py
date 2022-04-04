from behave import given, when, then, step

from pyspark.sql import functions as f


@given('I have {number:d} rupees')
def step_impl(context, number):
    context.amount = number


@given('I have {number} items')
def step_impl(context, number):
    context.items_count = float(number)


@when('I buy the following items')
def step_impl(context):
    rows = [row.cells for row in context.table]
    df = context.session.createDataFrame(rows, context.table.headings)

    # Update the money left
    df = df.withColumn('Expense', f.col('Quantity') * f.col('Price'))
    print('test')
    print(df.agg({'Expense': 'sum'}).collect())
    expense = df.agg({'Expense': 'sum'}).collect()[0][0]
    print(expense)
    context.amount = context.amount - expense

    # Update the amount of items
    count_bought_item = df.agg({'Quantity': 'sum'}).collect()[0][0]
    context.items_count += count_bought_item


@when('I sell the following items')
def step_impl(context):
    rows = [row.cells for row in context.table]
    df = context.session.createDataFrame(rows, context.table.headings)

    # Update the money left
    df = df.withColumn('Profit', f.col('Quantity') * f.col('Price'))
    profit = df.agg({'Profit': 'sum'}).collect()[0][0]
    context.amount = context.amount + profit

    # Update the amount of items
    count_sold_items = df.agg({'Quantity': 'sum'}).collect()[0][0]
    context.items_count = context.items_count - count_sold_items


@then('I should have {number:d} rupees left')
def step_impl(context, number):
    assert (context.amount == number)


@then('I should have {number:d} items in all')
def step_impl(context, number):
    assert (context.items_count == number)
