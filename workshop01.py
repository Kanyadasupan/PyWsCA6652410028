def countWords(sentence):
    showwords = sentence.split()
    totalWords = len(showwords)
    
    unionWords = set(showwords)
    totalUnique = len(unionWords)
    
    duplicateWords = [word for word in unionWords if showwords.count(word) > 1]
    
    print(f"มีคำรวมทั้งหมด {totalWords} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(duplicateWords)} คำ คือ {' '.join(duplicateWords)}")
    
    for word in duplicateWords:
        count = showwords.count(word)
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")

try:
    inputSenTence = input("ป้อนประโยค: ")
    countWords(inputSenTence)
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")







