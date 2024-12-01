# misread the instructions:

# # def find_matches_in_(l_one: list, l_two: list):
# #     count = 0
# #     catch = None # catch the num
# #     print(l_one)
# #     temp_two = l_two.copy()
# #     for i in l_one:
# #         if catch is None:
# #             if i in temp_two:
# #                 count += 1
# #                 catch = i
# #                 temp_two.remove(i)
# #                 print(i)
# #                 print(count)
# #         elif catch in temp_two:
# #             count += 1
# #             temp_two.remove(catch)
# #     if catch is not None:
# #         return catch, count
# #     return None, None


# # def remove_every_value_of_num_for_(list, num):
# #     temp_l = list.copy()
# #     for i in list:
# #         if i == num:
# #             temp_l.remove(i)
# #     return temp_l


# # def calculate_similarity_scores(list_one, list_two):
# #     """
# #     For example (from AoC):

# #     The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
# #     The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
# #     The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
# #     The fourth number, 1, also does not appear in the right list.
# #     The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
# #     The last number, 3, appears in the right list three times; the similarity score again increases by 9.

# #     So, for each "same number" match we get, we should add that number?

# #     NO, been reading it wrong. Should only look at the first list and multiple down
# #     """
# #     similar_score = 0
# #     temp_one = list_one.copy()
# #     temp_two = list_two.copy()

# #     for i in range(len(list_one)):  # list_one should be the same length as list_two as we curated them from the same text file
# #         #print(list_one)
# #         int_match, amount = find_matches_in_(temp_one, temp_two)

# #         print(f"int match: {int_match}")
# #         print(f"amount: {amount}")

# #         if int_match:
# #             print(f"times: {(int_match * amount)}")
# #             similar_score += (int_match * amount)

# #             # int_match was in both lists, so remove them
# #             temp_one = remove_every_value_of_num_for_(temp_one, int_match)
# #             temp_two = remove_every_value_of_num_for_(temp_two, int_match)
# #             # temp_one.remove(int_match)
# #             # temp_two.remove(int_match)
# #         print("-----")
# #     return similar_score

################################################################

# def find_matches_in_(l_one: list, l_two: list):
#     count = 0
#     catch = None  # to catch the num
#     temp_two = l_two.copy()

#     for i in l_one:
#         if catch is None:
#             if i in temp_two:
#                 count += 1
#                 catch = i
#                 temp_two.remove(i)

#     for i in temp_two:
#         if i == catch:
#             count += 1
#             temp_two.remove(i)

#     if catch is not None:
#         return catch, count

#     return None, None

# def calculate_similarity_scores(list_one, list_two):
#     """
#     Calculates a score by comparing list_one to list_two.

#     23184381 is wrong...
#     """
#     similar_score = 0
#     temp_one = list_one.copy()
#     temp_two = list_two.copy()

#     for i in range(len(list_one)):  # list_one should be the same length as list_two as we curated them from the same text file
#         #print(list_one)
#         int_match, amount = find_matches_in_(temp_one, temp_two)

#         print(f"int match: {int_match}")
#         print(f"amount: {amount}")

#         if int_match:
#             print(f"times: {(int_match * amount)}")
#             similar_score += (int_match * amount)

#             # .remove() removes the 'first occurrence of value.', which is good enough without having to sort the list out
#             temp_one.remove(int_match)
#         # print("-----")
#     return similar_score