/* 
 * File:   system.h
 * Author: Quentin
 *
 * Created on 04 nobember 2015, 23:01
 */

#ifndef SYSTEM_H
#define	SYSTEM_H

#ifdef	__cplusplus
extern "C" {
#endif

/******************************************************************************/
/******************************** INCLUDES ************************************/
/******************************************************************************/
    #include <libpic30.h>
    #include <p33FJ128MC804.h>
    #include <xc.h>
    #include <stdint.h>
    #include <stdlib.h>
    #include <math.h>
    #include <stdbool.h>
    #include "pwm.h"

    
/******************************************************************************/
/***************************** Defines ****************************************/
/******************************************************************************/


    //Macro pour les tempos
#define FOSC        7370000LL     //80017142LL      //80000000
#define FCY             (FOSC/2)
#define delay_us(x) __delay32(((x*FCY)/1000000L))   // delays x us
#define delay_ms(x) __delay32(((x*FCY)/1000L))      // delays x ms


/******************************************************************************/
/********************************* TIMERS *************************************/
/******************************************************************************/

#define ACTIVE                  0b1
#define DESACTIVE               0b0
    
#define LED                     0
#define SERVO                   1
#define LED_ROUGE               2
    
#define FRONT_MONTANT           0
#define FRONT_DESCENDANT        1

#define TIMER_5ms               T1CONbits.TON
#define TIMER_10ms              T4CONbits.TON
#define TIMER_90s               T2CONbits.TON
#define TIMER_DEBUG             T5CONbits.TON

#define FLAG_TIMER_5ms          IFS0bits.T1IF
#define FLAG_TIMER_10ms         IFS1bits.T4IF
#define FLAG_TIMER_90s          IFS0bits.T3IF
#define FLAG_TIMER_DEBUG        IFS1bits.T5IF

/******************************************************************************/
/********************************  PORT CARTE   *******************************/
/******************************************************************************/

#define BOUTON1             PORTCbits.RC9
#define BOUTON2             PORTCbits.RC8
#define BOUTON3             PORTCbits.RC7
#define BOUTON4             PORTBbits.RB6
    
#define SENS_MOTEUR         PORTCbits.RC0

#define CAPTEUR             PORTCbits.RC1
#define ENABLE_CAPTEUR      PORTCbits.RC2
    
#define ENABLE_BL           PORTCbits.RC6
#define STATUS_BL           PORTBbits.RB7
    
//#define LED1_PWM
#define LED1                LATBbits.LATB12
#define LED2                LATAbits.LATA10
#define LED3                LATAbits.LATA7
#define LED4                LATAbits.LATA0
#define LED5                LATAbits.LATA1
#define LED6                LATBbits.LATB0
#define LED7                LATBbits.LATB1
#define LED8                LATBbits.LATB2
#define LED9                LATBbits.LATB3

/******************************************************************************/
/******************************* Interruptions  *******************************/
/******************************************************************************/


/******************************************************************************/
/******************************* Interruptions  *******************************/
/******************************************************************************/
    
#define FRONT_INT0          FRONT_MONTANT
#define FRONT_INT1          FRONT_MONTANT
#define FRONT_INT2          FRONT_MONTANT
    
//#define UTILISATION_INT_CAPTEUR
//#define UTILISATION_INT_BOUTON1
//#define UTILISATION_INT_BOUTON2
//#define UTILISATION_INT_BOUTON3
//#define UTILISATION_INT_STATUS_BL

#define PRIO_INTER_TIMER1               0   // 
#define PRIO_INTER_TIMER2               0   // 
#define PRIO_INTER_TIMER3               0   // 
#define PRIO_INTER_TIMER4               0   // 
#define PRIO_INTER_TIMER5               0   // 
#define PRIO_INTER_UART1_RX             0   // USB RECEPTION
#define PRIO_INTER_UART1_TX             0   // USB TRANSMISSION
#define PRIO_INTER_UART2_RX             0   // BLE RECEPTION
#define PRIO_INTER_UART2_TX             0   // BLE TRANSMISSION
#define PRIO_INTER_INT0                 0   // INT0 : SATUS BL
#define PRIO_INTER_INT1                 0   // INT1 : CAPTEUR
#define PRIO_INTER_INT2                 7   // INT2 : BOUTON X
#define PRIO_INTER_I2C_MAITRE           0   // I�C d�sactiv� pour le moment
#define PRIO_INTER_I2C_ESCLAVE          0   // I�C d�sactiv� pour le moment
#define PRIO_INTER_QEI                  0   // CODEUR : prio la plus haute

#define ACTIV_INTER_TIMER1              0   // Timer asserv 
#define ACTIV_INTER_TIMER2              0   // Timer
#define ACTIV_INTER_TIMER3              0   // Timer 
#define ACTIV_INTER_TIMER4              0   // Timer 
#define ACTIV_INTER_TIMER5              0   // Timer 
#define ACTIV_INTER_UART1_RX            0   // UART USB : 
#define ACTIV_INTER_UART1_TX            0   // UART USB : type inter
#define ACTIV_INTER_UART2_RX            0   // UART BLE 
#define ACTIV_INTER_UART2_TX            0   // UART BLE : type inter
#define ACTIV_INTER_INT0                0   // INT0 : STATUS BL
#define ACTIV_INTER_INT1                0   // INT1 : CAPTEUR
#define ACTIV_INTER_INT2                0   // INT2 : BOUTON X
#define ACTIV_INTER_I2C_MAITRE          0   // Pas impl�ment� pour le moment
#define ACTIV_INTER_I2C_ESCLAVE         0   // Pas impl�ment� pour le moment
#define ACTIV_INTER_QEI                 0   // CODEUR


/******************************************************************************/
/*************************** Variables Globales *******************************/
/******************************************************************************/


/******************************************************************************/
/****************************** Prototypes ************************************/
/******************************************************************************/

    void ConfigADC (void);

    /**
     * Fonction qui initialise tous les syst�mes de la carte
     * Uart, Timer, PWM, mapping ....
     */
    void init_system (void);
    

    /**
     * Fonction qui configure toutes les interruptions
     * Ainsi que les priorit�s
     */
    void ConfigInterrupt (void);


    /**
     * Fonction qui configure toures les broches entr�es sorties
     */
    void ConfigPorts (void);


    /**
     * Configure le mappage des modules sp�ciaux : UART, QEI
     */
    void ConfigMapping (void);
    
    
    /**
    * Desactivation de tous les modules innutiles pour r�duire la consommation
    *      1 = DESACTIVE
    *      0 = ACTIVE (par d�faut)
    */
   void config_energie (void);
    
    
    void config_timer_5ms();

    

#ifdef	__cplusplus
}
#endif

#endif	/* SYSTEM_H */

