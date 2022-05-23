class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        _logs = [log.split(' ') for log in logs]
        letters_logs = []
        digits_logs = []
        result = []
        
        for log in _logs:
            if log[1].isdigit():
                digits_logs.append(log)
            else:
                letters_logs.append(log)
        
        letters_logs.sort(key=lambda x:(x[1:], x[0]))
        
        for log in letters_logs:
            result.append(' '.join(log))
        for log in digits_logs:
            result.append(' '.join(log))
        
        return result;

        