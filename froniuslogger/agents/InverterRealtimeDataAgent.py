from froniuslogger.agents import BaseAgent


class InverterRealtimeDataAgent(BaseAgent):

    @property
    def endpoint_name(self):
        return 'GetInverterRealtimeData.cgi'