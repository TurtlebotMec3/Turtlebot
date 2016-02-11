/* 
 * File:   interruptions.h
 * Author: Quentin
 *
 * Created on 8 novembre 2015, 15:42
 */

#ifndef INTERRUPTIONS_H
#define	INTERRUPTIONS_H

/******************************************************************************/
/***************************** Defines ****************************************/
/******************************************************************************/

/******************************************************************************/
/****************************** Prototypes ************************************/
/******************************************************************************/

/**
 *  Interruption du Timer 1 : Asserv
 */
void __attribute__((__interrupt__, no_auto_psv)) _T1Interrupt(void);


void __attribute__((__interrupt__, no_auto_psv)) _INT2Interrupt(void);
#endif	/* INTERRUPTIONS_H */

