from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoInscritosEnMesa(self, id_mesa):
        theQuery = {"numero_mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    def getListadoInscritosEnCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    def getMayorVotosCandidato(self):
        query1={
                "$group": {
                    "_id": "$numero_mesa",
                        "max": {
                        "$max": "$votos"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)

    def getVotosCandidatos(self):
        query1 = {
                "$group": {
                    "_id": "$candidato",
                        "sum": {
                                "$sum": "$votos"
                                 }
                          }
                }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

