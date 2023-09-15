class mission:
    def _init_(self):
        self.direc_sat = 'N' # Initial direction (N, S, E, W, U, D)
        self.position = [0, 0, 0]
        self.prev = 'N'


    def sat_move(self, command, dir):
        if command == 'f':   
            if dir == 'N':
                self.position[1] += 1
            elif dir == 'S':
                self.position[1] -= 1
            elif dir == 'E':
                self.position[0] += 1
            elif dir == 'W':
                self.position[0] -= 1
            elif dir == 'U':
                self.position[2] += 1
            elif dir == 'D':
                self.position[2] -= 1
        elif command == 'b':
            if dir == 'N':
                self.position[1] -= 1
            elif dir == 'S':
                self.position[1] += 1
            elif dir == 'E':
                self.position[0] -= 1
            elif dir == 'W':
                self.position[0] += 1
            elif dir == 'U':
                self.position[2] -= 1
            elif dir == 'D':
                self.position[2] += 1
    
    def sat_turning(self, command, dir):
        if command == 'l':
            if dir == 'N':
                self.direc_sat = 'W'
            elif dir == 'S':
                self.direc_sat = 'E'
            elif dir == 'E':
                self.direc_sat = 'N'
            elif dir == 'W':
                self.direc_sat = 'S'
            elif dir == 'U':
                self.sat_turning(command, self.prev)
            elif dir == 'D':
                self.sat_turning(command, self.prev)
        elif command == 'r':
            if dir == 'N':
                self.direc_sat = 'E'
            elif dir == 'S':
                self.direc_sat = 'W'
            elif dir == 'E':
                self.direc_sat = 'S'
            elif dir == 'W':
                self.direc_sat = 'N'
            elif dir == 'U':
                self.sat_turning(command, self.prev)
            elif dir == 'D':
                self.sat_turning(command, self.prev)
            

    def sat_tilted(self, command, dir):
        if command == 'u': 
            if dir == 'N':
                self.prev = 'N'  #storing for turn purpose
                self.direc_sat = 'U'
            elif dir == 'S':
                self.prev = 'S'
                self.direc_sat = 'U'
            elif dir == 'E':
                self.prev = 'E'
                self.direc_sat = 'U'
            elif dir == 'W':
                self.prev = 'W'
                self.direc_sat = 'U'
            else:
                self.direc_sat = 'U'
        elif command == 'd':
            if dir == 'N':
                self.prev = 'N'
                self.direc_sat = 'D'
            elif dir == 'S':
                self.prev = 'S'
                self.direc_sat = 'D'
            elif dir == 'E':
                self.prev = 'E'
                self.direc_sat = 'D'
            elif dir == 'W':
                self.prev = 'W'
                self.direc_sat = 'D'
            else:
                self.direc_sat = 'D'

    def execution(self, commands):
        for c in commands:
            if c in ('f', 'b'):
                self.sat_move(c, self.direc_sat)
            elif c in ('l', 'r'):
                self.sat_turning(c, self.direc_sat)
            elif c in ('u', 'd'):
                self.sat_tilted(c, self.direc_sat)
            

    def getPos(self):
        return self.position

    def getDirection(self):
        return self.direc_sat