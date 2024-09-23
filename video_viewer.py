from datetime import datetime, timedelta


class Video:

    def __init__(self, len: datetime, pos: datetime, op_start: datetime, op_end: datetime):
        self.len = len
        self.pos = pos
        self.op_start = op_start
        self.op_end = op_end

    def get_pos_str(self) -> str:
        return f"{self.pos.minute:02d}:{self.pos.second:02d}"

    def receive_command(self, command: str):
        if self.in_opening:
            self.skip_opening()
        if command == "next":
            self.next()
        elif command == "prev":
            self.prev()
        if self.in_opening:
            self.skip_opening()

    def next(self) -> None:
        self.pos = min(self.len, self.pos + timedelta(seconds=10))


    def prev(self) -> None:
        self.pos = max(datetime(year=self.pos.year, month=self.pos.month, day=self.pos.day, hour=self.pos.hour, minute=0, second=0), self.pos - timedelta(seconds=10))

    def skip_opening(self) -> None:
        self.pos = self.op_end

    @property
    def in_opening(self) -> bool:
        return self.op_start <= self.pos < self.op_end


def solution(video_len, pos, op_start, op_end, commands):
    """
    https://school.programmers.co.kr/learn/courses/30/lessons/340213
    :param video_len:
    :param pos:
    :param op_start:
    :param op_end:
    :param commands:
    :return:
    """
    video = Video(
        datetime(year=2024, month=9, day=18, hour=1, minute=int(video_len[0:2]), second=int(video_len[3:5])),
        datetime(year=2024, month=9, day=18, hour=1, minute=int(pos[0:2]), second=int(pos[3:5])),
        datetime(year=2024, month=9, day=18, hour=1, minute=int(op_start[0:2]), second=int(op_start[3:5])),
        datetime(year=2024, month=9, day=18, hour=1, minute=int(op_end[0:2]), second=int(op_end[3:5])),
    )
    for command in commands:
        video.receive_command(command)

    return video.get_pos_str()


print(solution("34:33","13:00","00:55","02:55",["next", "prev"]))
