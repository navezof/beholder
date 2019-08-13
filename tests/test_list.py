import beholder


def assert_equal(test_name, obtained_result, expected_result):
    if obtained_result == expected_result:
        print(test_name + " - OK")
    else:
        print(test_name + " - NOK\n\texpected: " + "".join(expected_result), "\n\tobtained: " + "".join(obtained_result))

def test_list_regression():
    # Verify user can get one item from every table
    testGetItemWeapon1()
    testGetItemWeapon2()

    testGetItemArmor1()
    testGetItemArmor2()

    # Verify user can get the full list of every table
    testListAll()

    # Verify the user can list the content of a specific table
    testListArmorTable1()
    testListArmorTable2()

    testListWeaponTable1()
    testListWeaponTable2()

    testListAll()

    # Verify the user can list all available tables
    test_list_all_tables()

    # Verify the user can get all item using a specific value in a table
    test_list_ranged_weapon1()
    test_list_ranged_weapon_2()
    test_list_ranged_weapon_3()
    test_list_ranged_weapon_4()

    testListImperiumWeapon1()

    testListMeleeWeapon1()

    testListFlakArmor1()
    testListAR4Armor()

def test_list_ranged_weapon1():
    command = ["weapons", "ranged"]
    expected_result = ["--- weapons (ranged) ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)"]
    beholder.execute(command)
    assert_equal("testListRangedWeapon1", beholder.result, expected_result)
    beholder.result.clear()


def test_list_ranged_weapon_2():
    command = ["list", "ranged"]
    expected_result = ["--- armors (ranged) ---",
                       "flak coat - AR:3",
                       "--- weapons (ranged) ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)"]
    beholder.execute(command)
    assert_equal("testListRangedWeapon2", beholder.result, expected_result)
    beholder.result.clear()


def test_list_ranged_weapon_3():
    command = ["list", "weapons", "ranged"]
    expected_result = ["--- weapons (ranged) ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)"]
    beholder.execute(command)
    assert_equal("testListRangedWeapon3", beholder.result, expected_result)
    beholder.result.clear()


def test_list_ranged_weapon_4():
    command = ["list", "weapons", "type", "ranged"]
    expected_result = ["--- weapons (type: ranged) ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)"]
    beholder.execute(command)
    assert_equal("testListRangedWeapon4", beholder.result, expected_result)
    beholder.result.clear()


def testListImperiumWeapon1():
    command = ["list", "imperium"]
    expected_result = ["--- armors (imperium) ---",
                       "flak coat - AR:3",
                       "flak vest - AR:3",
                       "--- weapons (imperium) ---",
                       "shotgun - damage:10+1ED (spread)",
                       "power axe - damage:12+2ED (force)"]
    beholder.execute(command)
    assert_equal("testListImperiumWeapon1", beholder.result, expected_result)
    beholder.result.clear()


def testListMeleeWeapon1():
    command = ["list", "melee"]
    expected_result = ["--- armors (melee) ---",
                       "--- weapons (melee) ---",
                       "power sword - damage:10+1ED (force)",
                       "power axe - damage:12+2ED (force)"]
    beholder.execute(command)
    assert_equal("testListMeleeWeapon1", beholder.result, expected_result)
    beholder.result.clear()


def testListFlakArmor1():
    command = ["list", "flak"]
    expected_result = ["--- armors (flak) ---",
                       "flak coat - AR:3",
                       "flak vest - AR:3",
                       "--- weapons (flak) ---"]
    beholder.execute(command)
    assert_equal("testListFlakArmor1", beholder.result, expected_result)
    beholder.result.clear()


def testListAR4Armor():
    command = ["list", "armor rating", "4"]
    expected_result = ["--- armors (armor rating: 4) ---",
                       "plate armor - AR:4",
                       "--- weapons (armor rating: 4) ---"]
    beholder.execute(command)
    assert_equal("testListAR4Armor", beholder.result, expected_result)
    beholder.result.clear()


def testGetItemWeapon1():
    command = ["lasgun"]
    expected_result = ["lasgun - damage:7+1ED (steadfast)"]
    beholder.execute(command)
    assert_equal("testGetItemWeapon 1", beholder.result, expected_result)
    beholder.result.clear()
    command.clear()


def testGetItemWeapon2():
    command = ["power sword"]
    expected_result = ["power sword - damage:10+1ED (force)"]
    beholder.execute(command)
    assert_equal("testGetItemWeapon 2", beholder.result, expected_result)
    beholder.result.clear()
    command.clear()


def testGetItemArmor1():
    command = ["flak coat"]
    expected_result = ["flak coat - AR:3"]
    beholder.execute(command)
    assert_equal("testGetItemArmor 1", beholder.result, expected_result)
    beholder.result.clear()


def testGetItemArmor2():
    command = ["plate armor"]
    expected_result = ["plate armor - AR:4"]
    beholder.execute(command)
    assert_equal("testGetItemArmor2", beholder.result, expected_result)
    beholder.result.clear()


def testListArmorTable1():
    command = ["list", "armors"]
    expected_result = ["--- armors ---",
                       "flak coat - AR:3",
                       "flak vest - AR:3",
                       "plate armor - AR:4"]
    beholder.execute(command)
    assert_equal("testListArmorTable 1", beholder.result, expected_result)
    beholder.result.clear()


def testListArmorTable2():
    command = ["armors"]
    expected_result = ["--- armors ---",
                       "flak coat - AR:3",
                       "flak vest - AR:3",
                       "plate armor - AR:4"]
    beholder.execute(command)
    assert_equal("testListArmorTable 2", beholder.result, expected_result)
    beholder.result.clear()


def testListWeaponTable1():
    command = ["list", "weapons"]
    expected_result = ["--- weapons ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)",
                       "power sword - damage:10+1ED (force)",
                       "power axe - damage:12+2ED (force)"]
    beholder.execute(command)
    assert_equal("testListWeaponTable 1", beholder.result, expected_result)
    beholder.result.clear()


def testListWeaponTable2():
    command = ["weapons"]
    expected_result = ["--- weapons ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)",
                       "power sword - damage:10+1ED (force)",
                       "power axe - damage:12+2ED (force)"]
    beholder.execute(command)
    assert_equal("testListWeaponTable 2", beholder.result, expected_result)
    beholder.result.clear()


def testListAll():
    command = ["list"]
    expected_result = ["--- armors ---",
                       "flak coat - AR:3",
                       "flak vest - AR:3",
                       "plate armor - AR:4",
                       "--- weapons ---",
                       "shotgun - damage:10+1ED (spread)",
                       "lasgun - damage:7+1ED (steadfast)",
                       "bolt pistol - damage:7+1ED (brutal pistol)",
                       "power sword - damage:10+1ED (force)",
                       "power axe - damage:12+2ED (force)"]
    beholder.execute(command)

    assert_equal("testListAll 1", beholder.result, expected_result)
    beholder.result.clear()


def test_list_all_tables():
    command = ["tables"]
    expected_result = ["--- armors ---", "--- weapons ---"]
    beholder.execute(command)
    assert_equal("testListAllTables 1", beholder.result, expected_result)
    beholder.result.clear()


if __name__ == "__main__":
    beholder.setup("../")
    test_list_regression()