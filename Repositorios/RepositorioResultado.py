from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoInscritosEnCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    def getListadoInscritosEnMesa(self, id_mesa):
        theQuery = {"numero_mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    def getResultadosEnMesas(self):

        query1 = {
            "$group": {
                "_id": "$numero_mesa",
                "suma": {
                    "$sum": "$votos"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)