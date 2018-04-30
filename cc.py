def is_all_digits(cc_num):
  # check if all characters are numbers
  for char in cc_num:
    if char not in "0123456789":
      return False
  return True

def is_16_length(cc_num):
  return len(cc_num) == 16

def clean_number(cc_num):
  cleaned_cc = ""
  for char in cc_num:
    # if char != "-" and char != " ":
    if char not in " -":
      cleaned_cc = cleaned_cc + char
  return cleaned_cc

def is_valid_cc(cc_num):
  cleaned_cc = clean_number(cc_num)
  return is_all_digits(cleaned_cc) and is_16_length(cleaned_cc)
