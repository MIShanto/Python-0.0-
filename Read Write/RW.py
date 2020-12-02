rF = open("E://Python-0.0-//Read Write//readTry.txt", "r")
wF = open("E://Python-0.0-//Read Write//writeTry.txt", "w")
with open("E://Python-0.0-//Read Write//writeTry.txt", "a") as aF:

    for lines in rF:
        wF.write(lines)
        tokens = lines.split(' ')

    wF.write("\nwords length: "+ str(len(tokens)))

    aF.write("\t\t\n\n ........Write Succesfull........")
    rF.close()
    wF.close()
