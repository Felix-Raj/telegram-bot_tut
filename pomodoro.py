class Pomodoro:
    def __init__(self, pomodoro_time=25*60, short_break=5*60,
                 long_break=10*60, cycle=3):
        self.pomodoro_time = pomodoro_time
        self.short_break = short_break
        self.long_break = long_break
        self.cycle = cycle
        self.start_state = PomodoroState(pomodoro_time, message='In Pomodoro')
        self.current_state = self.start_state
        self.create_states()

    def create_states(self):
        current_state = self.start_state
        for _ in range(self.cycle):
            current_state.next_state = PomodoroState(self.short_break,
                                                     message='Take Short Break')
            current_state.next_state.next_state = PomodoroState(
                self.pomodoro_time, message='In Pomodoro')
            current_state = current_state.next_state.next_state
        current_state.next_state = PomodoroState(self.long_break,
                                                 self.start_state,
                                                 'Take Long Break')

    def next_state(self):
        _next_state = self.current_state.next_state
        self.current_state = _next_state
        return _next_state


class PomodoroState:
    def __init__(self, time_out, next_state=None, message=None):
        self.time_out = time_out
        self.next_state = next_state
        self._message = message

    def message(self):
        if self._message:
            return self._message
        return 'Next reminder in {} minutes'.format(self.time_out/60)
