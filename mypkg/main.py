from pdfparser import PDFParser
from docxparser import DocxParser
from docoleparser import DocOleParser
#from docconverterparser import DocConverterParser
from htmlparser import HTMLParser
from pdfminerparser import PDFMinerParser
from docxxmlparser import DocxXMLParser


def pdfminer():
    pdf_parser = PDFMinerParser()
    pdf_parser.parse(r'files/Test3.pdf')
    print('pdfminer parser', pdf_parser.get_processed_stems(), len(pdf_parser.get_processed_stems()))


def pdf():
    pdf_parser = PDFParser()
    pdf_parser.parse(r'files/Test3.pdf')
    print('pdf parser', pdf_parser.get_processed_stems(), len(pdf_parser.get_processed_stems()))


def docx():
    docx_parser = DocxParser()
    docx_parser.parse(r'files/Test2.docx')
    print('docx parser', docx_parser.get_processed_stems(), len(docx_parser.get_processed_stems()))


def docx_xml():
    docx_xml_parser = DocxXMLParser()
    docx_xml_parser.parse(r'files/Test2.docx')
    print('docx_xml parser', docx_xml_parser.get_processed_stems(), len(docx_xml_parser.get_processed_stems()))


def doc_ole():
    doc_ole_parser = DocOleParser()
    doc_ole_parser.parse(r'files/Test2.doc')
    print('doc_ole parser', doc_ole_parser.get_processed_stems(), len(doc_ole_parser.get_processed_stems()))


def doc_converter():
    doc_parser = DocConverterParser()
    doc_parser.parse(r'files/Test2.doc')
    print('doc_converter parser', doc_parser.get_processed_stems(), len(doc_parser.get_processed_stems()))


def html():
    html_parser = HTMLParser()
    html_parser.parse(r'files/Test2.html')
    print('html parser', html_parser.get_processed_stems(), len(html_parser.get_processed_stems()))
    print('html parser link result', html_parser.get_links(), len(html_parser.get_links()))


if __name__ == '__main__':
    pdf() # 1
    pdfminer() # 47294
    docx_xml() # 47294
    docx() # 47294
    doc_ole() # not working  418466
#    doc_converter()
    html() # 47312 #0