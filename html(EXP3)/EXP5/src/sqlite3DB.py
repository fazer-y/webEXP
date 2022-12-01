# -*- coding: utf-8 -*-
import sqlite3


class sqlite3DB:
    def __init__(self, DBFilePath) -> None:
        self.dbPath = DBFilePath

    def Open(self):
        connector = sqlite3.connect(self.dbPath)
        return connector

    def __GetSql(self, sql):
        conn = self.Open()
        cur = conn.cursor()
        cur.execute(sql)
        fields = []
        for field in cur.description:
            fields.append(field[0])

        result = cur.fetchall()
        cur.close()
        return result, fields

    def Close(self, conn):
        conn.close()

    def GetSql(self, sql):
        conn = self.Open()
        result, fields = self.__GetSql(sql)
        self.Close(conn)
        return result, fields

    def UpdateData(self, sql):
        conn = self.Open()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        self.Close(conn)

    def InsertData(self, sql, values):
        conn = self.Open()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        self.Close(conn)

    def DeleteDataById(self, id, value, tablename):
        conn = self.Open()
        cursor = conn.cursor()
        sql = "delete from %s  where %s=?" % (tablename, id)
        cursor.execute(sql, (value,))
        conn.commit()
        cursor.close()
        self.Close(conn)
