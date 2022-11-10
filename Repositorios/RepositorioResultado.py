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

    def promedioNotasEnMateria(self, id_materia):
        query1 = {
            "$match": {"materia.$id": ObjectId(id_materia)}
        }
        query2 = {
            "$group": {
                "_id": "$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)