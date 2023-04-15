import pandaStore

if __name__ == "__main__":
    columns = ["time", "voltage", "current", "temp"]

    record = pandaStore.Record(columns)

    data = {
        "time" : "dd/mm/yy 00:00:00",
        "data" : {
            "voltage" : 175,
            "temp" : 42
        }
    }

    record.appendData(data)

    data = {
        "time" : "dd/mm/yy 00:00:00",
        "data" : {
            "current" : 0.2,
            "temp" : 38
        }
    }

    record.appendData(data)

    record.appendData(data)

    data = {
        "time" : "dd/mm/yy 00:00:00",
        "data" : {
            "resistance" : 10000,
            "temp" : 38
        }
    }

    record.appendData(data)

    record.showDataHead()
    record.showAllData()
    record.saveData("Redbird_test_data.json")

    record2 = pandaStore.Record()
    record2.loadData("Redbird_test_data.json")
    record2.showAllData()
