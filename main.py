import sys
from Clinic import Clinic
from Logistic import Logistic
from Supplier import Supplier
from Vaccine import Vaccine
from Repository import repo


def main(args):
    repo.create_tables()

    total_inventory = 0
    total_demand = 0
    total_received = 0
    total_sent = 0

    maxID = 0

    f = open(args[1], 'r')
    firstLine = f.readline()
    firstLineSplitter = firstLine.split(",")
    i = 0
    for numTable in firstLineSplitter:
        intNum = int(numTable)
        while intNum > 0:
            line = f.readline()
            splitLine = line.split(",")
            if i == 0:
                repo.vaccines.insert(Vaccine(splitLine[0], splitLine[1], splitLine[2], splitLine[3]))
                total_inventory = total_inventory + int(splitLine[3])
                if (int(splitLine[0])) > maxID:
                    maxID = int(splitLine[0])
            elif i == 1:
                repo.suppliers.insert(Supplier(splitLine[0], splitLine[1], splitLine[2]))
            elif i == 2:
                repo.clinics.insert(Clinic(splitLine[0], splitLine[1], splitLine[2], splitLine[3]))
                total_demand = total_demand + int(splitLine[2])
            else:
                repo.logistics.insert(Logistic(splitLine[0], splitLine[1], splitLine[2], splitLine[3]))
            intNum = intNum - 1
        i = i + 1
    f.close()

    outputFile = open("output.txt", "w")

    with open(args[2], 'r') as inputfile:
        for line in inputfile:
            splitter = line.split(",")
            if len(splitter) == 2:  # sending
                id = repo.clinics.find(splitter[0]).id
                demand = repo.clinics.find(splitter[0]).demand
                sendDemand = int(splitter[1])
                sd = sendDemand
                repo.clinics.update(id, demand - sendDemand)

                while sendDemand > 0:
                    quantity = repo.vaccines.find().quantity
                    id = repo.vaccines.find().id
                    subtration = sendDemand - quantity
                    if subtration < 0:
                        repo.vaccines.update(id, (-1) * subtration)
                        sendDemand = 0
                    else:
                        repo.vaccines.delete(id)
                        sendDemand = subtration

                newCountSent = repo.logistics.find(repo.clinics.find(splitter[0]).logistic).count_sent + sd
                total_sent = total_sent + sd
                total_demand = total_demand - sd
                total_inventory = total_inventory - sd
                repo.logistics.updateSent(repo.clinics.find(splitter[0]).logistic, newCountSent)
            else:  # recieve
                date = splitter[2]
                quantity = int(splitter[1])
                supplier = repo.suppliers.find(splitter[0]).id
                maxID = maxID + 1
                repo.vaccines.insert(Vaccine(maxID, date, supplier, quantity))

                newCountRec = repo.logistics.find(repo.suppliers.find(splitter[0]).logistic).count_received + quantity
                total_received = total_received + quantity
                total_inventory = total_inventory + quantity
                repo.logistics.updateRec(repo.suppliers.find(splitter[0]).logistic, newCountRec)

            outputFile.write(
                ','.join([str(total_inventory), str(total_demand), str(total_received), str(total_sent)])+"\n")


if __name__ == '__main__':
    main(sys.argv)
