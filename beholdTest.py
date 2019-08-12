class BeholdTest():

    def assertEqual(self, testName, result, expectedResult):
        if (result == expectedResult):
            print(testName + " - OK")
        else:
            print(testName + " - NOK\n\texpected: " + "".join(expectedResult), "\n\tobtained: " + "".join(result))

    def regression(self):
        #Verify user can get one item from every table
        self.testGetItemWeapon1()
        self.testGetItemWeapon2()

        self.testGetItemArmor1()
        self.testGetItemArmor2()

        #Verify user can get the full list of every table
        self.testListAll()

        #Verify the user can list the content of a specific table
        self.testListArmorTable1()
        self.testListArmorTable2()

        self.testListWeaponTable1()
        self.testListWeaponTable2()

        self.testListAll()
        
        #Verify the user can list all available tables
        self.testListAllTables()

        #Verify the user can get all item using a specific value in a table
        self.testListRangedWeapon1()
        self.testListRangedWeapon2()
        self.testListRangedWeapon3()
        self.testListRangedWeapon4()

        self.testListImperiumWeapon1()

        self.testListMeleeWeapon1()

        self.testListFlakArmor1()
        self.testListAR4Armor()
        
    def testAll(self):
        
        self.regression()
        
        
    def testListRangedWeapon1(self):
        command = ["weapons", "ranged"]
        expectedResult = ["--- weapons (ranged) ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)"]
        execute(command)
        self.assertEqual("testListRangedWeapon1", result, expectedResult)
        result.clear()

    def testListRangedWeapon2(self):
        command = ["list", "ranged"]
        expectedResult = ["--- armors (ranged) ---",
                          "flak coat - AR:3",
                          "--- weapons (ranged) ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)"]
        execute(command)
        self.assertEqual("testListRangedWeapon2", result, expectedResult)
        result.clear()

    def testListRangedWeapon3(self):
        command = ["list", "weapons", "ranged"]
        expectedResult = ["--- weapons (ranged) ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)"]
        execute(command)
        self.assertEqual("testListRangedWeapon3", result, expectedResult)
        result.clear()

    def testListRangedWeapon4(self):
        command = ["list", "weapons", "type", "ranged"]
        expectedResult = ["--- weapons (type: ranged) ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)"]
        execute(command)
        self.assertEqual("testListRangedWeapon4", result, expectedResult)
        result.clear()

    def testListImperiumWeapon1(self):
        command = ["list", "imperium"]
        expectedResult = ["--- armors (imperium) ---",
                          "flak coat - AR:3",
                          "flak vest - AR:3",
                          "--- weapons (imperium) ---",
                          "shotgun - damage:10+1ED (spread)",
                          "power axe - damage:12+2ED (force)"]
        execute(command)
        self.assertEqual("testListImperiumWeapon1", result, expectedResult)
        result.clear()

    def testListMeleeWeapon1(self):
        command = ["list", "melee"]
        expectedResult = ["--- armors (melee) ---",
                          "--- weapons (melee) ---",
                          "power sword - damage:10+1ED (force)",
                          "power axe - damage:12+2ED (force)"]
        execute(command)
        self.assertEqual("testListMeleeWeapon1", result, expectedResult)
        result.clear()
        
    def testListFlakArmor1(self):
        command = ["list", "flak"]
        expectedResult = ["--- armors (flak) ---",
                          "flak coat - AR:3",
                          "flak vest - AR:3",
                          "--- weapons (flak) ---"]
        execute(command)
        self.assertEqual("testListFlakArmor1", result, expectedResult)
        result.clear()

    def testListAR4Armor(self):
        command = ["list", "armor rating", "4"]
        expectedResult = ["--- armors (armor rating: 4) ---",
                          "plate armor - AR:4",
                          "--- weapons (armor rating: 4) ---"]
        execute(command)
        self.assertEqual("testListAR4Armor", result, expectedResult)
        result.clear()
    
    def testGetItemWeapon1(self):
        command = ["lasgun"]
        expectedResult = ["lasgun - damage:7+1ED (steadfast)"]
        execute(command)
        self.assertEqual("testGetItemWeapon 1", result, expectedResult)
        result.clear()
        command.clear()

    def testGetItemWeapon2(self):
        command = ["power sword"]
        expectedResult = ["power sword - damage:10+1ED (force)"]
        execute(command)
        self.assertEqual("testGetItemWeapon 2", result, expectedResult)
        result.clear()
        command.clear()

    def testGetItemArmor1(self):
        command = ["flak coat"]
        expectedResult = ["flak coat - AR:3"]
        execute(command)
        self.assertEqual("testGetItemArmor 1", result, expectedResult)
        result.clear()

    def testGetItemArmor2(self):
        command = ["plate armor"]
        expectedResult = ["plate armor - AR:4"]
        execute(command)
        self.assertEqual("testGetItemArmor2", result, expectedResult)
        result.clear()

    def testListArmorTable1(self):
        command = ["list", "armors"]
        expectedResult = ["--- armors ---",
                          "flak coat - AR:3",
                          "flak vest - AR:3",
                          "plate armor - AR:4"]
        execute(command)
        self.assertEqual("testListArmorTable 1", result, expectedResult)
        result.clear()

    def testListArmorTable2(self):
        command = ["armors"]
        expectedResult = ["--- armors ---",
                          "flak coat - AR:3",
                          "flak vest - AR:3",
                          "plate armor - AR:4"]
        execute(command)
        self.assertEqual("testListArmorTable 2", result, expectedResult)
        result.clear()        

    def testListWeaponTable1(self):
        command = ["list", "weapons"]
        expectedResult = ["--- weapons ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)",
                          "power sword - damage:10+1ED (force)",
                          "power axe - damage:12+2ED (force)"]
        execute(command)
        self.assertEqual("testListWeaponTable 1", result, expectedResult)
        result.clear()

    def testListWeaponTable2(self):
        command = ["weapons"]
        expectedResult = ["--- weapons ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)",
                          "power sword - damage:10+1ED (force)",
                          "power axe - damage:12+2ED (force)"]
        execute(command)
        self.assertEqual("testListWeaponTable 2", result, expectedResult)
        result.clear()

    def testListAll(self):
        command = ["list"]
        expectedResult = ["--- armors ---",
                          "flak coat - AR:3",
                          "flak vest - AR:3",
                          "plate armor - AR:4",
                          "--- weapons ---",
                          "shotgun - damage:10+1ED (spread)",
                          "lasgun - damage:7+1ED (steadfast)",
                          "bolt pistol - damage:7+1ED (brutal pistol)",
                          "power sword - damage:10+1ED (force)",
                          "power axe - damage:12+2ED (force)"]
        execute(command)
        
        self.assertEqual("testListAll 1", result, expectedResult)
        result.clear()
        
    def testListAllTables(self):
        command = ["tables"]
        expectedResult = ["--- armors ---", "--- weapons ---"]
        execute(command)
        self.assertEqual("testListAllTables 1", result, expectedResult)
        result.clear()
