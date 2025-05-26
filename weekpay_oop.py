import pymysql


class WeekPayManager:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost", user="user02", password="----", db="----", port=3306
        )
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def insert(self):
        wname = input("이름: ")
        whour = int(input("근무시간 : "))
        pay = int(input("시간당 급여액 : "))
        overpay, total = self.calculate_pay(whour, pay)

        sql = """
            insert into weekpay(wname, whour, pay, overpay, total)
            values (%s, %s, %s, %s, %s)            
        """
        self.curs.execute(sql, (wname, whour, pay, overpay, total))
        self.conn.commit()

    def update(self):
        self.output()
        id = int(input("수정할 아이디는?"))
        wname = input("수정할 이름 : ")
        whour = int(input("수정할 근무시간 : "))
        pay = int(input("수정할 시간당 급여액 : "))
        overpay, total = self.calculate_pay(whour, pay)

        sql = """
            update weekpay
            set wname = %s, whour = %s, pay = %s, overpay = %s, total = %s
            where id = %s
        """
        self.curs.execute(sql, (wname, whour, pay, overpay, total, id))
        self.conn.commit()

    def delete(self):
        self.output()
        id = int(input("삭제할 아이디는?"))

        sql = "delete from weekpay where id=%s"
        self.curs.execute(sql, (id,))
        self.conn.commit()

    def output(self):
        print("***** week pay *****")
        sql = "select * from weekpay"
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        for row in rows:
            print(
                row["id"],
                row["wname"],
                row["whour"],
                row["pay"],
                row["overpay"],
                row["total"],
            )

    def calculate_pay(self, whour, pay):
        if whour > 20:
            overpay = (whour - 20) * pay * 1.5
            total = whour * pay * 1.2 + overpay
            return overpay, total

        else:
            overpay = 0
            total = whour * pay
            return overpay, total

    def close(self):
        self.conn.close()


def main():
    manager = WeekPayManager()
    while True:
        sel = input(" 1.목록 2.추가 3.수정 4.삭제 0.종료 : ")
        if sel == "1":
            manager.output()
        elif sel == "2":
            manager.insert()
        elif sel == "3":
            manager.update()
        elif sel == "4":
            manager.delete()
        elif sel == "0":
            manager.close()
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()
