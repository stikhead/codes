import log_analyzer as la

error_list = la.extract_errors(la.mock_logs)
print(error_list)
print(la.count_erros(error_list))