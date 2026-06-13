
from crewai import Agent,Crew,Process,Task
from crewai.project import CrewBase,agent,crew,task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class StockPicker():
    """ Stock Picker Crew """

    agents:list[BaseAgent]
    tasks:list[Task]

    @agent
    def market_analyst(self)->Agent:

        return Agent(
            config=self.agents_config['market_analyst'],
            verbose=True
        )


    @agent
    def risk_analyst(self)->Agent:

        return Agent(
            config=self.agents_config['risk_analyst'],
            verbose=True
        )

    @agent
    def stock_picker(self)->Agent:

        return Agent(
            config=self.agents_config['stock_picker'],
            verbose=True
        )

    @task
    def market_analyst_task(self)->Task:

        return Task(
            config=self.tasks_config['market_analyst_task']
        )

    @task
    def risk_analysis_task(self)->Task:

        return Task(
            config=self.tasks_config['risk_analysis_task']
        )
    
    @task
    def stock_picker_task(self)->Task:

        return Task(
            config=self.tasks_config['stock_picker_task'],
            output_file='stock_report.md'
        )

    @crew
    def crew(self)->Crew:
        """creates stock picker Crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

    









