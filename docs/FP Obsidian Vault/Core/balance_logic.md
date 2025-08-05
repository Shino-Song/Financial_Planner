This file holds the logic for calculating and estimating the balance of the account(s). It does *not* store data. Balance data is stored in a separate files organized by month and fiscal year.

balance_logic is designed to work as follows.
1. Take input of actual balance.
2. Create and modify files for balance data.
3. Estimate balance based on current expenses.
4. Validate estimated balance against actual balance and report discrepancies.
5. Project future balances using historical expense, income, and deduction estimates.

Code -

