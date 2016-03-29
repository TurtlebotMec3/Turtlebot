/******************************************************************************/
/***************** CARTE BALISE : DSPIC33FJ128MC804 ***************************/
/******************************************************************************/
/* Fichier 	: pwm.c
 * Auteur  	: Quentin
 * Revision	: 1.0
 * Date		: 08 novembre 2015, 15:30
 *******************************************************************************
 *
 *
 ******************************************************************************/

/******************************************************************************/
/******************************** INCLUDES ************************************/
/******************************************************************************/

#include "system.h"

/******************************************************************************/
/**************************** Configurations Des PWM **************************/
/******************************************************************************/


void ConfigPWM (void)
{
	//****************
	//PWM
	//****************
	P1TCONbits.PTEN		= 1;		//PWM1 ON
    P2TCONbits.PTEN     = 1;        //PWM2 ON
    
    
    P1TCONbits.PTSIDL   = 1;        //continu en idle
    P1TCONbits.PTOPS    = 0;        //Postscaller 1 : 1
    P1TCONbits.PTCKPS   = 0;        //Prescaller  1 : 1
    
    P2TCONbits.PTSIDL   = 1;        //continu en idle
    P2TCONbits.PTOPS    = 0;        //Postscaller 1 : 1
    P2TCONbits.PTCKPS   = 1;        //Prescaller  1 : 4

	P1TCONbits.PTMOD	= 0;		//Base de temps en free running mode (11 bits vmax = 2048)
	P2TCONbits.PTMOD	= 0;		//Base de temps en free running mode (11 bits vmax = 2048)

    P1TPER              = 999;	
    P2TPER              =  18424;	//F=50Hz 15.6 bits
 
    PWM1CON1bits.PMOD1 = 1;
    PWM1CON1bits.PMOD2 = 1;
    PWM1CON1bits.PMOD3 = 1;
    PWM2CON1bits.PMOD1 = 1;
    
    
    
    PWM1CON1bits.PEN1H	= 1;		//PWM1H1 pour led bleu du turtlebot
	PWM1CON1bits.PEN1L	= 0;		//PWM1L1 inactif => I/O
	PWM1CON1bits.PEN2H	= 0;		//PWM1H2 pour PWM_GAUCHE
	PWM1CON1bits.PEN2L	= 1;		//PWM1L2 pour led rouge du turtlebot
	PWM1CON1bits.PEN3H	= 0;		//PWM1H3 pour pour PWM_DROIT
	PWM1CON1bits.PEN3L	= 0;		//PWM1L3 inactif => I/O
    
	PWM2CON1bits.PEN1H	= 1;		//PWM2H1 inactif => I/O
	PWM2CON1bits.PEN1L	= 0;		//PWM2L1 pour servo caméra


	// Mise a zero des PWM
    PDC1 = 0;
    PDC2 = 0;
    
}


/******************************************************************************/
/******************************** MODFIFS PWM *********************************/
/******************************************************************************/

void envoit_pwm (double valeur, uint8_t module)
{
    if (valeur > 100)
        valeur = 100;
    else if (valeur < 0)
        valeur = 0;


    if (module == SERVO)
    {
        //de 0 à 100%
        //  50% = 1.5 ms
        //   0% = 1.0 ms
        // 100% = 2.0 ms  
        valeur /= 100;
        valeur += 1;

        //résulat en ms, maintenant conversion en valeur pwm

        valeur *= PWM_MAX_VALUE / 20;

        if (valeur > PWM_MAX_VALUE)
            valeur = PWM_MAX_VALUE;

        P2DC1 = (uint16_t) valeur;
    }
    else if (module == LED)
    {
        valeur *= PWM_MAX_LED / 100;
        PDC1 = (uint16_t) valeur;
    }
    else if (module == LED_ROUGE)
    {
        valeur *= PWM_MAX_LED / 100;
        PDC2 = (uint16_t) valeur;
    }
}

/******************************************************************************/
/******************************************************************************/
/******************************************************************************/
