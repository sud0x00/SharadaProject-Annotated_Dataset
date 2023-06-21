
from indic_transliteration import sanscript

def devanagari_to_itrans(devanagari_text):
    itrans_text = sanscript.transliterate(devanagari_text, sanscript.DEVANAGARI, sanscript.ITRANS)
    return itrans_text

# Example usage:
dev=["-","fs","अ","ऋ","ए","क","कृ","क्षि","ग","गा","गी","गे","गो","ग्रे","घ्न","घ्ने","ङ्खो","च","च्या","ज","णः","णा","त","ता","ति","ती","त्मा","त्रे","त्वा","द","दी","दृ","दे","द्द","द्म","द्वि","धि","धिं","न","नः","ना","नु","न्ता","न्त्र","न्दः","न्दि","न्मौ","न्व","न्वे","न्सिं","प","पा","पी","पु","पू","प्छ","भ","भा","भे","भ्र","म","मः","मा","मे","मो","म्","य","या","यु","ये","र","रः","रा","र्ण","र्त्रे","र्म","ल","ला","लि","ले","ल्य","व","वा","वां","वि","वी","व्या","श","शु","शू","शृ","शो","श्या","श्री","श्व","ष","षिः","षु","ष्क","ष्टु","ष्णाः","स","स्त्वं","स्य","ह","हि","ॐ","१"]

# Convert Devanagari texts to ITRANS
itrans_texts = [devanagari_to_itrans(text) for text in dev]

# Save ITRANS texts to a text file
output_file = 'C:/NLP Sanskrit/temp2/file.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for itrans_text in itrans_texts:
        file.write(itrans_text + '\n')
