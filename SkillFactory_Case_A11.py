#!/usr/bin/env python
#
import pandas as pd

TESTS_FILE='/tmp/Case_A11/ab_test_groups.csv.bz2'
PAYMENTS_FILE='/tmp/Case_A11/payments.csv.bz2'
TEST_ID=127
START_DATE='2019-08-05'
END_DATE='2019-08-12'  # This day will not be included

test_uids_df = pd.read_csv(TESTS_FILE)
test_uids_df = test_uids_df[test_uids_df.ab_test_id==127].reset_index()
group_a_st = set(test_uids_df.loc[test_uids_df.grp == 'A', 'user_id'])
group_b_st = set(test_uids_df.loc[test_uids_df.grp == 'B', 'user_id'])
# print(group_a_st.intersection(group_b_st))

payments_df = pd.read_csv(PAYMENTS_FILE)
payments_df = payments_df.loc[payments_df.created_at.between(START_DATE, END_DATE, inclusive=False)]

abtest_df = payments_df.loc[:,('user_id', 'price')]
