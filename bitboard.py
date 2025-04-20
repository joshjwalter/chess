class Bitboard:
    def __init__(self):
        # these are the bitboards for each type of piece
        # TODO: also maybe add en passant squares (youtube video)
        # TODO: should i create special moves like castling and en passant in this file or the higher level file?

        self.white_pawns = 0
        self.white_knights = 0
        self.white_bishops = 0
        self.white_rooks = 0
        self.white_queens = 0
        self.white_king = 0
        self.black_pawns = 0
        self.black_knights = 0
        self.black_bishops = 0
        self.black_rooks = 0
        self.black_queens = 0
        self.black_king = 0

        # bitboards for each color
        ## works by ORing all the pieces together
        ### this is used to check if a square is occupied by a piece of the same color

        self.white_pieces = 0
        for x in [self.white_pawns, self.white_knights, self.white_bishops, self.white_rooks, self.white_queens, self.white_king]: 
            self.white_pieces |= x
        self.black_pieces = 0
        for x in [self.black_pawns, self.black_knights, self.black_bishops, self.black_rooks, self.black_queens, self.black_king]: 
            self.black_pieces |= x

        # array of all bitboards
        self.board_array = [self.white_pawns, self.white_knights, self.white_bishops, self.white_rooks, self.white_queens, self.white_king,
                            self.black_pawns, self.black_knights, self.black_bishops, self.black_rooks, self.black_queens, self.black_king, self.white_pieces, self.black_pieces]

    def sync_boards(self):
        for x in [self.white_pawns, self.white_knights, self.white_bishops, self.white_rooks, self.white_queens, self.white_king]:
            self.white_pieces |= x
        for x in [self.black_pawns, self.black_knights, self.black_bishops, self.black_rooks, self.black_queens, self.black_king]:
            self.black_pieces |= x

    def clear_square(self, square):
        # EXAMPLE: x&= ~(1 << square)
        ## this line creates a number with all bits 0 except for the square that is being cleared
        ### it then flips all the bits in the number and ANDs it with the bitboard which clears the bit
        self.white_pawns &= ~(1 << square)
        self.white_knights &= ~(1 << square)
        self.white_bishops &= ~(1 << square)
        self.white_rooks &= ~(1 << square)
        self.white_queens &= ~(1 << square)
        self.white_king &= ~(1 << square)

        self.black_pawns &= ~(1 << square)
        self.black_knights &= ~(1 << square)
        self.black_bishops &= ~(1 << square)
        self.black_rooks &= ~(1 << square)
        self.black_queens &= ~(1 << square)
        self.black_king &= ~(1 << square)
    
        self.sync_boards()
        
    def move_piece(self, color, piece, start_square, end_square):
        ### WARNING: this function does not check for move availability!!!
        # EXAMPLE: self.color_piece |= 1 << end_square
        ## This line creates a number with all bits 0 except for the end square set to 1
        ### it then ORs it with the bitboard which turns on the bit for the end square

        if (color in ["white", "black"]) and (piece in ["pawn", "knight", "bishop", "rook", "queen", "king"]):
            # clear the start square
            self.clear_square(start_square)
            # clear the end square
            self.clear_square(end_square)
            # turn on end square in color bitboard
            match color:
                case "white":
                    self.white_pawns |= 1 << end_square
                case "black":
                    self.black_pawns |= 1 << end_square
            # turn on end square in piece bitboard
            match piece:
                case "pawn":
                    if color == "white":
                        self.white_pawns |= 1 << end_square
                    elif color == "black":
                        self.black_pawns |= 1 << end_square
                case "knight":
                    if color == "white":
                        self.white_knights |= 1 << end_square
                    elif color == "black":
                        self.black_knights |= 1 << end_square
                case "bishop":
                    if color == "white":
                        self.white_bishops |= 1 << end_square
                    elif color == "black":
                        self.black_bishops |= 1 << end_square
                case "rook":
                    if color == "white":
                        self.white_rooks |= 1 << end_square
                    elif color == "black":
                        self.black_rooks |= 1 << end_square
                case "queen":
                    if color == "white":
                        self.white_queens |= 1 << end_square
                    elif color == "black":
                        self.black_queens |= 1 << end_square
                case "king":
                    if color == "white":
                        self.white_king |= 1 << end_square
                    elif color == "black":
                        self.black_king |= 1 << end_square
                case _:
                    raise Exception("Invalid Piece Type ( bitboard.py, move_piece() )")
        else:
            raise Exception("Invalid Piece Color ( bitboard.py, move_piece() )")

    def output_index(self, bit_byte):
        #creates an integer with only the bit flipped we are checking, does an and check and appends to final array if the result is greater than 1
        found = []
        for y in range(64):
            if (bit_byte & (1 << y)) > 0:
                found.append(y)
        return found