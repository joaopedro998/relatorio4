from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()


def clienteB(self):
         jsonCB = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id"},
                    "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$match": {"_id.cliente": "B"}},
])
        return jsonCB
 def produtoMenosV(self):
        jsonPV = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
])
        return jsonPV
 def clienteMenosG(self):
        jsonMG = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": 1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])
        return jsonMG
def listaProdutos(self):
    jsonLP = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 2}}},
        {"$group": {"_id": "$produtos.nome"}},
    ])
    return jsonLP



