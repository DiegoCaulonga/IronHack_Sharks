def cleaner(time):
    try :
        return re.findall(r"\d{2}h00",time)[0]
    except :
        return None