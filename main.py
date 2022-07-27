import random

import ciw

class_names = ["peygiri sefaresh", "darkhast peyk", "moshahede restoran web", "moshahede restoran mobile",
               "ersal payam peyk", "sabt sefaresh web", "sabt sefaresh mobile"]
node_names = ["web", "api", "payment", "peyk", "sefaresh", "moshtari", "restoran"]

# inputs:
servers_number = [1, 1, 1, 2, 5, 3, 2]
priority_class = [1, 0, 1, 1, 1, 0, 0]
class_error_rate = [0.01, 0.01, 0.2, 0.1, 0.03, 0.02, 0.02]
class_arrival_prob = [0.05, 0.20, 0.15, 0.25, 0.05, 0.10, 0.20]
landa = 20
max_wait_time = [25, 30, 25, 30, 30, 40, 20]


def define_network(servers_number, class_error_rates, priority_class, class_arrival_prob, landa, max_wait_time):
    # servers order:
    e1 = lambda x: class_error_rates[0]
    e2 = lambda x: class_error_rates[1]
    e3 = lambda x: class_error_rates[2]
    e4 = lambda x: class_error_rates[3]
    e5 = lambda x: class_error_rates[4]
    e6 = lambda x: class_error_rates[5]
    e7 = lambda x: class_error_rates[6]
    reneging_dist = {'Class 0': [ciw.dists.Deterministic(max_wait_time[0]) for i in range(7)],
                     'Class 1': [ciw.dists.Deterministic(max_wait_time[1]) for i in range(7)],
                     'Class 2': [ciw.dists.Deterministic(max_wait_time[2]) for i in range(7)],
                     'Class 3': [ciw.dists.Deterministic(max_wait_time[3]) for i in range(7)],
                     'Class 4': [ciw.dists.Deterministic(max_wait_time[4]) for i in range(7)],
                     'Class 5': [ciw.dists.Deterministic(max_wait_time[5]) for i in range(7)],
                     'Class 6': [ciw.dists.Deterministic(max_wait_time[6]) for i in range(7)],
                     }
    service_dist = [ciw.dists.Exponential(rate=1 / 3),
                    ciw.dists.Exponential(rate=1 / 2),
                    ciw.dists.Exponential(rate=1 / 12),
                    ciw.dists.Exponential(rate=1 / 9),
                    ciw.dists.Exponential(rate=1 / 6),
                    ciw.dists.Exponential(rate=1 / 5),
                    ciw.dists.Exponential(rate=1 / 8)]

    arrival_dist_peygiri = [ciw.dists.NoArrivals(),
                            ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[0])),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals()]
    arrival_dist_peyk = [ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[1])),
                         ciw.dists.NoArrivals(),
                         ciw.dists.NoArrivals(),
                         ciw.dists.NoArrivals(),
                         ciw.dists.NoArrivals(),
                         ciw.dists.NoArrivals(),
                         ciw.dists.NoArrivals()]
    arrival_dist_det_web = [ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[2])),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals(),
                            ciw.dists.NoArrivals()]
    arrival_dist_det_mobile = [ciw.dists.NoArrivals(),
                               ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[3])),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals()]
    arrival_dist_peyk_payam = [ciw.dists.NoArrivals(),
                               ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[4])),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals(),
                               ciw.dists.NoArrivals()]
    arrival_dist_order_web = [ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[5])),
                              ciw.dists.NoArrivals(),
                              ciw.dists.NoArrivals(),
                              ciw.dists.NoArrivals(),
                              ciw.dists.NoArrivals(),
                              ciw.dists.NoArrivals(),
                              ciw.dists.NoArrivals()]
    arrival_dist_order_mobile = [ciw.dists.NoArrivals(),
                                 ciw.dists.Exponential(rate=1 / (landa * class_arrival_prob[6])),
                                 ciw.dists.NoArrivals(),
                                 ciw.dists.NoArrivals(),
                                 ciw.dists.NoArrivals(),
                                 ciw.dists.NoArrivals(),
                                 ciw.dists.NoArrivals()]

    route_dist_peygiri = [[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0]]

    route_dist_peyk = [[0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0]]

    route_dist_det_web = [[0, 0, 0, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0]]

    route_dist_det_mobile = [[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]]

    route_dist_peyk_payam = [[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]]

    route_dist_order_web = [[0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]]

    route_dist_order_mobile = [[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0]]

    N = ciw.create_network(
        arrival_distributions={'Class 0': arrival_dist_peygiri,
                               'Class 1': arrival_dist_peyk,
                               'Class 2': arrival_dist_det_web,
                               'Class 3': arrival_dist_det_mobile,
                               'Class 4': arrival_dist_peyk_payam,
                               'Class 5': arrival_dist_order_web,
                               'Class 6': arrival_dist_order_mobile,
                               },
        service_distributions={'Class 0': service_dist,
                               'Class 1': service_dist,
                               'Class 2': service_dist,
                               'Class 3': service_dist,
                               'Class 4': service_dist,
                               'Class 5': service_dist,
                               'Class 6': service_dist,
                               },
        baulking_functions={'Class 0': [e1 for i in range(7)], 'Class 1': [e2 for i in range(7)],
                            'Class 2': [e3 for i in range(7)], 'Class 3': [e4 for i in range(7)],
                            'Class 4': [e5 for i in range(7)],
                            'Class 5': [e6 for i in range(7)], 'Class 6': [e7 for i in range(7)]},
        routing={'Class 0': route_dist_peygiri,
                 'Class 1': route_dist_peyk,
                 'Class 2': route_dist_det_web,
                 'Class 3': route_dist_det_mobile,
                 'Class 4': route_dist_peyk_payam,
                 'Class 5': route_dist_order_web,
                 'Class 6': route_dist_order_mobile,
                 },
        number_of_servers=servers_number,

        priority_classes={'Class 0': priority_class[0], 'Class 1': priority_class[1], 'Class 2': priority_class[2],
                          'Class 3': priority_class[3], 'Class 4': priority_class[4], 'Class 5': priority_class[5],
                          'Class 6': priority_class[6]},
        reneging_time_distributions=reneging_dist
    )
    return N


def get_que_length_mean(recs, node_n, total_time):
    que_time_length = []
    for rec in recs:
        if rec.node == node_n:
            que_time_length.append((rec.arrival_date, rec.queue_size_at_arrival))
            que_time_length.append((rec.exit_date, rec.queue_size_at_departure))
    if len(que_time_length) == 0:
        return 0
    que_time_length = sorted(que_time_length, key=lambda tup: tup[0])
    sum_que_length = 0
    for i in range(len(que_time_length) - 1):
        l = (que_time_length[i + 1][1] + que_time_length[i][1]) / 2
        d_t = que_time_length[i + 1][0] - que_time_length[i][0]
        sum_que_length += l * d_t
    return sum_que_length / total_time


def wait_in_que_mean(recs):
    wait_times = [[] for i in range(7)]
    for rec in recs:
        wait_times[rec.customer_class].append(rec.waiting_time)
    class_wait_times = []
    for i in range(7):
        class_wait_times.append(sum(wait_times[i]) / len(wait_times[i]))
    all_mean_wait_time = sum(sum(wait_times, [])) / sum(len(l) for l in wait_times)
    return class_wait_times, all_mean_wait_time


def get_node_util(recs, node_id, node_number, total_time):
    util_time = 0
    for rec in recs:
        if rec.node == node_id and rec.service_time > 0:
            util_time += rec.service_time
    return (util_time / total_time) / node_number


def get_reneged_requests(id_rec_dict, total_costumers: list):
    reneged_requests = [0 for i in range(7)]
    for id_number in id_rec_dict:
        if id_rec_dict[id_number][0].record_type == "renege":
            reneged_requests[id_rec_dict[id_number][0].customer_class] += 1
    for i in range(7):
        reneged_requests[i] = reneged_requests[i] / total_costumers[i]
    all_mean_reneged_requests = sum(reneged_requests) / sum(total_costumers)
    return reneged_requests, all_mean_reneged_requests


def get_baulked_class(baulked_dict, total_costumers: list):
    baulked_class = [0 for i in range(7)]
    for node_id in baulked_dict:
        for i in range(7):
            baulked_class[i] += len(baulked_dict[node_id][i])
    for i in range(7):
        baulked_class[i] = baulked_class[i] / (total_costumers[i] + baulked_class[i])
    all_mean_baulked_class = sum(baulked_class) / (sum(total_costumers) + sum(baulked_class))
    return baulked_class, all_mean_baulked_class


total_time = 28000
ciw.seed(random.randint(0, 100))
Q = ciw.Simulation(define_network(servers_number, class_error_rate, priority_class, class_arrival_prob, landa, max_wait_time))
Q.simulate_until_max_time(total_time)

recs = Q.get_all_records()
id_rec_dict = dict()
times = []
total_costumers = [0, 0, 0, 0, 0, 0, 0]
for rec in recs:
    if rec.id_number not in id_rec_dict:
        id_rec_dict[rec.id_number] = [rec]
    else:
        id_rec_dict[rec.id_number].append(rec)
for id_number in id_rec_dict:
    total_costumers[id_rec_dict[id_number][0].customer_class] += 1

for i in range(1, 8):
    print("mean que length of node: ", node_names[i - 1], " ", get_que_length_mean(recs, i, total_time))
    node_util = get_node_util(recs, i, servers_number[i - 1], total_time)
    print("node util: ", get_node_util(recs, i, servers_number[i - 1], total_time))
    if node_util > 0.99:
        print("node ", node_names[i - 1], " is overloaded")
class_wait_times, all_mean_wait_time = wait_in_que_mean(recs)
for i in range(7):
    print("mean wait time in class: ", class_names[i], ": ", class_wait_times[i])
print("all mean wait time: ", all_mean_wait_time)
reneged_requests, all_mean_reneged_requests = get_reneged_requests(id_rec_dict, total_costumers)
for i in range(7):
    print("fraction of reneged requests in class: ", class_names[i], ": ", reneged_requests[i])
print("all mean reneged requests: ", all_mean_reneged_requests)
baulked_class, all_mean_baulked_class = get_baulked_class(Q.baulked_dict, total_costumers)
for i in range(7):
    print("fraction of baulked requests in class: ", class_names[i], ": ", baulked_class[i])
print("all mean baulked class: ", all_mean_baulked_class)
