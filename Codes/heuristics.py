class Heuristics:
	# When a choice between multiple operations is available, always pick the first one
	@staticmethod
	def select_first_operation(jobs_to_be_done, max_operations, _):
		best_candidates = {}

		for job in jobs_to_be_done:
			current_activity = job.current_activity
			best_operation = current_activity.shortest_operation

			if best_candidates.get(best_operation.id_machine) is None:
				best_candidates.update({best_operation.id_machine: [(current_activity, best_operation)]})
			elif len(best_candidates.get(best_operation.id_machine)) < max_operations:
				best_candidates.get(best_operation.id_machine).append((current_activity, best_operation))
			else:
				list_operations = best_candidates.get(best_operation.id_machine)

				for key, (_, operation) in enumerate(list_operations):
					if operation.duration < best_operation.duration:
						list_operations.pop(key)
						break

				if len(list_operations) < max_operations:
					list_operations.append((current_activity, best_operation))

		return best_candidates





	# Assign randomly jobs to machine
	@staticmethod
	def random_operation_choice(jobs_to_be_done, max_operations, _):
		import random
		best_candidates = {}
		dict_operations = {}

		for job in jobs_to_be_done:
			current_activity = job.current_activity
			for operation in current_activity.next_operations:
				if dict_operations.get(operation.id_machine) is None:
					dict_operations.update({operation.id_machine: [(current_activity, operation)]})
				else:
					dict_operations.get(operation.id_machine).append((current_activity, operation))

		for machine, list_operations in dict_operations.items():
			best_candidates.update({machine: list(
				set([list_operations[random.randint(0, len(list_operations) - 1)] for _ in range(max_operations)]))})

		return best_candidates

	## Creation of Machine assignment and operation sequence lists (need improvement)
	##
	@staticmethod
	def initialisation_list(jobs_to_be_done):
		machine_assignment = []
		operation_sequence = []
		for job in jobs_to_be_done:
			for activity in job.activities_to_be_done:
				operation_sequence.append(job.id_job)
				machine_assignment.append(activity.next_operations[0].id_machine)
		print("machine assignment :")
		for machine in machine_assignment:
			print(str(machine))
		print("operation sequence :")
		for operation in operation_sequence:
			print(operation)
