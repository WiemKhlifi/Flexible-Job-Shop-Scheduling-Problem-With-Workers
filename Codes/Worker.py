class Worker:
	def __init__(self, id_worker, max_operations):
		self.__id_worker = id_worker
		self.__is_working = False
		self.__operations_done = []
		self.__processed_operations = []
		self.__max_operations = max_operations
		self.__current_time = 0
		self.__available_places = [i for i in range(max_operations)]

	# Return the worker's id
	@property
	def id_worker(self):
		return self.__id_worker

	# Return the operations done by the worker
	@property
	def operations_done(self):
		return self.__operations_done

	# Return if the worker is working at max capacity
	def is_working_at_max_capacity(self):
		return len(self.__processed_operations) == self.__max_operations

	# Add an operation to the treatment list of the worker
	def add_operation(self, activity, operation):
		if self.is_working_at_max_capacity():
			raise EnvironmentError("worker already working at max capacity")
		if operation.id_worker != self.__id_worker:
			raise EnvironmentError("Operation assigned to the wrong worker")

		operation.time = self.__current_time
		operation.is_pending = True
		operation.place_of_arrival = self.__available_places.pop(0)

		self.__processed_operations.append((activity, operation))

	# Method to simulate a work process during one unit of time
	def work(self):
		self.__current_time += 1
		for activity, operation in self.__processed_operations:
			if operation.time + operation.duration <= self.__current_time:
				self.__processed_operations = list(filter(lambda element: not (
						element[0].id_job == activity.id_job and element[0].id_activity == activity.id_activity and
						element[1].id_operation == operation.id_operation), self.__processed_operations))
				self.__available_places.append(operation.place_of_arrival)
				activity.terminate_operation(operation)
				self.__operations_done.append(operation)
