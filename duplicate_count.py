def duplicate_count(text):
    return sum([1 for _i in set(list(text.lower())) if text.lower().count(_i)>=2])
    
print(duplicate_count("Indivisibilities"))