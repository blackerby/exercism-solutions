#lang racket

; Number -> Number
; computes the number of grains on a given square on a chessboard
(define (square n)
  (cond
    [(= n 1) 1]
    [else (expt 2 (- n 1))]))

(define (sum-squares n)
  (cond
    [(= n 0) 0]
    [else (+ (square n) (sum-squares (- n 1)))]))

(define (total)
  (sum-squares 64))

(provide square total)
    