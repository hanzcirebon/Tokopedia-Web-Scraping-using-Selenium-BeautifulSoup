from TokPed import Tokopedia

if __name__ == '__main__':
    tp = Tokopedia(keyword='laptop', totalPages=10)
    data = tp.run()
    tp.to_excel(data)