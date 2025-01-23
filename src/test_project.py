import pytest
from project import check, empty, row, column, block, allUsedNumList, usableNums

def test_check():
    with pytest.raises(ValueError, match="Invalid input"):
        check("abcdefg")
    with pytest.raises(ValueError, match="Invalid input"):
        check("........abc")
    with pytest.raises(ValueError, match="Invalid input"):
        check("0123456789")
    with pytest.raises(ValueError, match="Invalid input"):
        check(".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..")
    with pytest.raises(ValueError, match="Invalid input"):
        check(".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..61. 123")
    with pytest.raises(ValueError, match="Invalid input"):
        check(".34956.8.865..7.39..9.3...23..7.514.1..3.8..59.61......8..29..767....29....4..61.")
    with pytest.raises(ValueError, match="Invalid input"):
        check(".123.456#")

def test_row():
    line = ".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..61."
    allCellList = check(line)
    assert row(0, allCellList) == [3, 4, 9, 5, 6, 8]
    assert row(15, allCellList) == [8, 6, 5, 7, 3, 9]
    assert row(25, allCellList) == [9, 3, 2]

def test_column():
    line = ".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..61."
    allCellList = check(line)
    assert column(0, allCellList) == [8, 3, 1, 9, 6]
    assert column(15, allCellList) == [1, 2, 6]
    assert column(29, allCellList) == [4, 5, 9, 6]

def test_block():
    line = ".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..61."
    allCellList = check(line)
    assert block(0, allCellList) == [3, 4, 8, 6, 5, 9]
    assert block(6, allCellList) == [8, 3, 9, 2]
    assert block(12, allCellList) == [9, 5, 6, 7, 3]

def test_allUsedNumList():
    line = ".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..61."
    allCellList = check(line)
    assert allUsedNumList(0, allCellList) == {3, 9, 4, 8, 6, 1, 5}
    assert allUsedNumList(12, allCellList) == {3, 9, 4, 8, 7, 6, 1, 5}

def test_usableNums():
    line = ".34956.8. 865..7.39 ..9.3...2 3..7.514. 1..3.8..5 9.61..... .8..29..7 67....29. ...4..61."
    allCellList = check(line)
    assert usableNums(0, allCellList) == {2, 7}
    assert usableNums(12, allCellList) == {2}
